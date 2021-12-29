#!/usr/bin/env python3

# orchestrate the sudoku example
#
# pseudocode (simple nonparallel case)
# 
# while true:
#   guijob = gui.requestSudokuEvaluation(dummy1)
#   solverjob = evaluator.evaluateSudokuDesign(guijob)
#   aspresult = aspsolver.solve(solverjob)
#   evalresult = evaluator.processEvaluationResult(aspresult)
#   (dummy2 = )gui.processEvaluationResult(evalresult)

import logging
import json
import time
import grpc
import traceback
import sys

# generated from .proto
import orchestrator_pb2 as pb
import orchestrator_pb2_grpc as pb_grpc


logging.basicConfig(level=logging.DEBUG)


configfile = "config.json"
config = json.load(open(configfile, 'rt'))


def main():
    brokerconn = 'localhost:' + str(config['broker-grpcport'])
    roiconn = 'localhost:' + str(config['roi-grpcport'])
    yoloconn = 'localhost:' + str(config['yolo-grpcport'])
    latconn = 'localhost:' + str(config['lat-grpcport'])
    
    logging.info("connecting to Databroker at %s", brokerconn)
    broker_channel = grpc.insecure_channel(brokerconn)
    broker_stub = pb_grpc.ImageSourceStub(broker_channel)

    logging.info("connecting to ROI at %s", roiconn)
    roi_channel = grpc.insecure_channel(roiconn)
    roi_stub = pb_grpc.ImagePreProcessStub(roi_channel)

    logging.info("connecting to YOLO solver at %s", yoloconn)
    yolo_channel = grpc.insecure_channel(yoloconn)
    yolo_stub = pb_grpc.YOLOStub(yolo_channel)

    logging.info("connecting to LAT solver at %s", latconn)
    lat_channel = grpc.insecure_channel(latconn)
    lat_stub = pb_grpc.LabelStub(lat_channel)

    while True:
        try:
            logging.info("calling ImageSource.Get() with empty dummy")
            dummy1 = pb.Empty()
            brokerjob = broker_stub.Get(dummy1)

                
            try:
                logging.info("calling ImagePreProcess.RoadCrop() with brokerjob")
                roijob = roi_stub.RoadCrop(brokerjob)

                logging.info("calling YOLO.detect() with parameters roijob")
                yolojob = yolo_stub.Detect(roijob)

            except:
                logging.info("ROI server not started, skiping road crop step")
                logging.info("calling YOLO.detect() with parameters roijob")
                yolojob = yolo_stub.Detect(brokerjob)

            logging.info(
                "calling Label.Get() with yolojob")
            _ = lat_stub.Get(yolojob)

        except Exception as ex:
            if type(ex).__name__ == "_InactiveRpcError":
                logging.info("no more images")
                sys.exit()
                
            else:
                logging.error("exception (retrying after 2 seconds): %s", traceback.format_exc())
                # do not spam
                time.sleep(2)

main()
