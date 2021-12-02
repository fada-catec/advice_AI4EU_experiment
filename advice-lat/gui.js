function start(){

  threshold = 0

  document.getElementById("td_start").remove();

  $tr_menu = document.getElementById("tr_content_menu");
  $('<td id = "td_next"><button id = "next_bt" type="button" onclick="nextImage()">Next image</button></td>').appendTo($tr_menu)
  $('<td id = "td_all"><button id = "all_bt" type="button" onclick="copyAll()">Copy all & Next</button></td>').appendTo($tr_menu)
  $('<td id = "td_save"><button id = "save_bt" type="button" onclick="save()">Save</button></td>').appendTo($tr_menu)
  $('<td id = "td_discard"><button id = "discard_bt" type="button" onclick="discardChanges()">Discard changes</button></td>').appendTo($tr_menu)
  // $('<td id = "td_instructions"><button id = "instructions_bt" onmouseover="show()" onmouseout="hide()" type="button">Show instructions</button></td>').appendTo($tr_menu)
  $('<td id = "td_instructions"><button id = "instructions_bt" onclick="show()" type="button">Show instructions</button></td>').appendTo($tr_menu)

  $legend = document.getElementById("legend");
  $('<div class="legend-title">Legend</div><div class="legend-scale"><ul class="legend-labels"><li><span style="background:#cfcf38;"></span>KerbDeterioration</li><li><span style="background:#fa3253;"></span>Rutting</li><li><span style="background:#b83df5;"></span>Pothole</li><li><span style=background:#b25050;"></span>ManholeCover</li><li><span style="background:#21a84d;"></span>EdgeDeterioration</li><li><span style="background:#2a7dd1;"></span>Gully</li><li><span style="background:#000000;"></span>LooseStones</li></lu><br><lu><li><span style="background:#3d3df5;"></span>DefectiveSurfaceDressing</li><li><span style="background:#33e6ff;"></span>JointDefectiveness</li><li><span style="background:#ffcc33;"></span>ReflectionCracking</li><li><span style="background:#ff00cc;"></span>Settlement</li><li><span style="background:#aeb8b6;"></span>SurfaceDeterioration</li></ul>').appendTo($legend)


  saved_flag = true

  nextImage()

}

function instructions(){

steps_str = "STEP 1: Press the start button in order to launch the tool.\n\nSTEP 2: Click on the predicted labels that you want to be copied to the original image or you may want to copy all the predited labels, for that, press the middle button Copy all & Next.\n\nSTEP 3: If you choose manual mode, you have the option of clicking on the original image labels that you want to be deleted.\n\nSTEP 4: Save the new labels before continue, otherwise the tool won't let you press Next image button.\n\nSTEP 5:Press Next image button once you have saved to continue labeling"

alert(steps_str)
}

function nextImage(){

  if (saved_flag){

    saved_flag = false

    request().done(function(response){

      if(response == false){
        alert("No more images.\nPage will be reloaded.\nPress start button to labeling again.")
        exitFunction()
      }else{

        detection_labels = response[0]
        original_labels = response[1]
        orig_labels_no_change = [...response[1]]
        var img_path = "data:image/jpg;base64," + response[2]
        label_file_name = response[3]

        document.getElementById('act_img').innerHTML = label_file_name.split('.')[0];
        document.getElementById('index').innerHTML = response[4]+'/'+response[5];

        if (document.body.contains(document.getElementById('content'))) {
          document.getElementById('content').remove()
        }
        if (document.body.contains(document.getElementById('footing'))) {
          document.getElementById('footing').remove()
        }
        if (document.body.contains(document.getElementById('det_map'))) {
          document.getElementById('det_map').remove()
        }
        if (document.body.contains(document.getElementById('orig_map'))) {
          document.getElementById('orig_map').remove()
        }

        $('<table id="content"><tr><th>Predicted image</th><th>Original image</th></tr><tr><td><img class="map" id="det_img" src="'+img_path+'" alt="Predicted image" usemap="#predicted_label"></td><td><img class="map" id="orig_img" src="'+img_path+'" alt="Original image" usemap="#original_label"></td></tr></table>').appendTo('body');

        var $map = $('<map id="det_map" name="predicted_label">').appendTo('body');
        for (i=0;i<detection_labels.length;i++) {
          var coords = [detection_labels[i][1]/2, detection_labels[i][2]/2, (detection_labels[i][3] + detection_labels[i][1])/2, (detection_labels[i][4]+detection_labels[i][2])/2];
          $('<area id="det_label_'+ coords[0] + coords[1] +'" target="" alt="'+ detection_labels[i][0]+'" title="'+ detection_labels[i][0]+': '+detection_labels[i][5] +'" href="#" coords="'+ coords.toString() +'" shape="rect" onclick="addLabel(alt, coords)" />').appendTo($map);
        }
        
        var $map = $('<map id="orig_map" name="original_label">').appendTo('body');
        for (i=0;i<original_labels.length;i++) {
          var coords = [original_labels[i][1]/2, original_labels[i][2]/2, (original_labels[i][3] + original_labels[i][1])/2, (original_labels[i][4]+original_labels[i][2])/2];
          $('<area id="orig_label_'+ coords[0] + coords[1] +'" target="" alt="'+ original_labels[i][0] +'" title="'+ original_labels[i][0] +'" href="#" coords="'+ coords.toString() +'" shape="rect" onclick="deleteLabel(id, title, coords)" />').appendTo($map);
        }

        $(document).ready(function () {
            $('area').each(function () //get all areas
            {
                $(this).addClass("Cracking");
            });

          $('.map').maphilight({ alwaysOn: true});

          $(".Cracking").wrap(function () {
            //This block is what creates highlighting by trigger the "alwaysOn", 
            var data = $(this).data('maphilight') || {};
            data.strokeColor = colorClass($(this).attr("alt"));
            data.strokeWidth = 2;
            $(this).data('maphilight', data).trigger('alwaysOn.maphilight');
        }); 
    });
        
      $('<div id="footing"><hr><hr><p>Supported by AI4EU - A European AI On Demand Platform and Ecosystem. More information: <a href="https://www.ai4europe.eu">ai4europe.eu</a></p><table><tr><td><img id="EULogo" src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/Flag_of_Europe.svg/200px-Flag_of_Europe.svg.png" alt="EULogo"></td><td><p>This project has received funding from the European Union'+"'"+'s Horizon 2020</p><p>research and innovation programme under grant agreement 825619.</p></td></table></div>').appendTo('body')

      }
    });
  }else{
    alert("The image must be saved before continue.")
  }
}

function colorClass(class_defect){
  switch (class_defect){
      case 'KerbDeterioration':
          return 'cfcf38'
      case 'Rutting':
          return 'fa3253'
      case 'Pothole':
          return 'b83df5'
      case 'ManholeCover':
        return 'b25050'
      case 'EdgeDeterioration':
        return '21a84d'   
      case 'Gully':
        return '2a7dd1'
      case 'LooseStones':
        return '000000'    
      case 'DefectiveSurfaceDressing':
        return '3d3df5'
      case 'JointDefectiveness':
        return '33e6ff'
      case 'ReflectionCracking':
        return 'ffcc33'
      case 'Settlement':
        return 'ff00cc'
      case 'SurfaceDeterioration':
        return 'aeb8b6'                                                                                                                    
      default:
        return 'ffffff'
  }
}

function exitFunction(){

  if (document.body.contains(document.getElementById('det_map'))) {
    document.getElementById('det_map').remove()
  }
  if (document.body.contains(document.getElementById('orig_map'))) {
    document.getElementById('orig_map').remove()
  }
  if (document.body.contains(document.getElementById('td_next'))) {
    document.getElementById('td_next').remove()
  }
  if (document.body.contains(document.getElementById('td_all'))) {
    document.getElementById('td_all').remove()
  }
  if (document.body.contains(document.getElementById('td_save'))) {
    document.getElementById('td_save').remove()
  }
  if (document.body.contains(document.getElementById('td_instructions'))) {
    document.getElementById('td_instructions').remove()
  }
  if (document.body.contains(document.getElementById('td_discard'))) {
    document.getElementById('td_discard').remove()
  }
  if (document.body.contains(document.getElementById('counter'))) {
    document.getElementById('counter').remove()
  }
  if (document.body.contains(document.getElementById('content'))) {
    document.getElementById('content').remove()
  }

  $('<td id = "td_start"><button id = "start_bt" type="button" onclick="start()">Start</button></td>').appendTo($tr_menu)

  location.reload()
}

function copyAll(){
  save(all=true)
  nextImage()
}

function save(all){
  saved_flag = true
  if(all){

    for(i=0;i<detection_labels.length;i++){
      if (detection_labels[i][5]<threshold){
        detection_labels.splice(i)
      }else{
        detection_labels[i].pop() //Remove accuracy element of the array
      }
    }

    $.ajax({ type:'PUT', url: 'save_result?filename='+label_file_name+'&result='+detection_labels})
  }else{
    $.ajax({ type:'PUT', url: 'save_result?filename='+label_file_name+'&result='+original_labels})
  }
}

function discardChanges(){

  var $map = document.getElementById("orig_map");
  $map.remove();

  var $map = $('<map id="orig_map" name="original_label">').appendTo('body');
  for (i=0;i<orig_labels_no_change.length;i++) {
    var coords = [orig_labels_no_change[i][1]/2, orig_labels_no_change[i][2]/2, (orig_labels_no_change[i][3] + orig_labels_no_change[i][1])/2, (orig_labels_no_change[i][4]+orig_labels_no_change[i][2])/2];
    $('<area id="orig_label_'+ coords[0] + coords[1] +'" target="" alt="'+ orig_labels_no_change[i][0] +'" title="'+ orig_labels_no_change[i][0] +'" href="#" coords="'+ coords.toString() +'" shape="rect" onclick="deleteLabel(id, title, coords)" />').appendTo($map);
  }

  original_labels = [...orig_labels_no_change]

  $(document).ready(function () {
    $('area').each(function () //get all areas
    {
        $(this).addClass("Cracking");
    });

    $('.map').maphilight({ alwaysOn: true});

    $(".Cracking").wrap(function () {
      //This block is what creates highlighting by trigger the "alwaysOn", 
      var data = $(this).data('maphilight') || {};
      data.strokeColor = colorClass($(this).attr("alt"));
      data.strokeWidth = 2;
      $(this).data('maphilight', data).trigger('alwaysOn.maphilight');
    }); 

  });

  alert("All changes have been removed.")

}

function calculateIoU(det_coords, orig_coords){

  var det_coords = det_coords.split(",")

  var xA = Math.max(det_coords[0], orig_coords[0]);
  var yA = Math.max(det_coords[1], orig_coords[1]);
  var xB = Math.min(det_coords[2], orig_coords[2]);
  var yB = Math.min(det_coords[3], orig_coords[3]);

  var interArea = Math.abs(Math.max((xB-xA), 0)*Math.max((yB-yA), 0))

  if (interArea == 0){
    return 0
  }
  
  var boxAArea = Math.abs((det_coords[2]-det_coords[0]))*(det_coords[3]-det_coords[1])
  var boxBArea = Math.abs((orig_coords[2]-orig_coords[0]))*(orig_coords[3]-orig_coords[1])

  var iou_out = interArea / parseFloat(boxAArea + boxBArea - interArea)

  return iou_out;
}

function addLabel(title, det_coords) { 

  var existing_label = false;

  for (i=0;i<original_labels.length;i++) {
    if(title == original_labels[i][0]){

      var orig_coords = [original_labels[i][1]/2, original_labels[i][2]/2, (original_labels[i][3] + original_labels[i][1])/2, (original_labels[i][4]+original_labels[i][2])/2];
      var iou = calculateIoU(det_coords, orig_coords)

      if(iou >= 0.5){
        existing_label = true;
        break;
      }else{
        existing_label = false;
      }
    }
  }
  if(existing_label){
    alert("Label already exists in the original image. IoU = "+roundToTwo(iou));
  }else{
    saved_flag = false

    var $map = document.getElementById("orig_map");

    det_coords = det_coords.split(",");
    original_labels.push([title, det_coords[0]*2, det_coords[1]*2, (det_coords[2]-det_coords[0])*2, (det_coords[3]-det_coords[1])*2])

    $('<area id="new_label_'+ det_coords[0].toString() + det_coords[1].toString() +'" target="" alt="'+ title +'" title="'+ title +'" href="#" coords="'+ det_coords.toString() +'" shape="rect" onclick="deleteLabel(id, title, coords)" />').appendTo($map);
    
    $(document).ready(function () {
      $('area').each(function () //get all areas
      {
          $(this).addClass("Cracking");
      });

      $('.map').maphilight({ alwaysOn: true});

      $(".Cracking").wrap(function () {
          //This block is what creates highlighting by trigger the "alwaysOn", 
          var data = $(this).data('maphilight') || {};
          data.strokeColor = colorClass($(this).attr("alt"));
          data.strokeWidth = 2;
          $(this).data('maphilight', data).trigger('alwaysOn.maphilight');
        }); 
    });   
  }
}

function deleteLabel(id, title, coords){

  saved_flag = false

  document.getElementById(id).remove();

  coords = coords.split(",");

  for (i=0;i<original_labels.length;i++) {

    if(title == original_labels[i][0] && roundToTwo(coords[0]*2) == roundToTwo(original_labels[i][1]) && roundToTwo(coords[1]*2) == roundToTwo(original_labels[i][2]) && roundToTwo((coords[2]-coords[0])*2) == roundToTwo(original_labels[i][3]) && roundToTwo((coords[3]-coords[1])*2) == roundToTwo(original_labels[i][4])){
      original_labels.splice(i, 1)
      break;
    }
  }

  $(document).ready(function () {
    $('area').each(function () //get all areas
    {
        $(this).addClass("Cracking");
    });

    $('.map').maphilight({ alwaysOn: true});

    $(".Cracking").wrap(function () {
      //This block is what creates highlighting by trigger the "alwaysOn", 
      var data = $(this).data('maphilight') || {};
      data.strokeColor = colorClass($(this).attr("alt"));
      data.strokeWidth = 2;
      $(this).data('maphilight', data).trigger('alwaysOn.maphilight');
    }); 
  });   

}

function request() {
  return $.ajax({
    type: "GET",
    url: 'request',
    success: function(result) {
    },
    failure: function(errMsg){
    }
  });
}

function show() {

  document.getElementById("instructions_bt").remove()

  $('<td id = "td_instructions"><button id = "instructions_bt" onclick="hide()" type="button">Hide instructions</button></td>').appendTo($tr_menu)

  var $instructionPopUp = document.getElementById("instructionPopUp");

  $('<table id="instruction_table"><tr><td id="step"><a style="font-weight:bold;">STEP 1:</a></td><td >Press the start button in order to launch the tool.</td></tr><tr><td id="step"><a style="font-weight:bold;">STEP 2:</a></td><td>Click on the predicted labels that you want to be copied to the original image or you may want to copy all the <br>predicted labels, for that, press the middle button "Copy all & Next".</td></tr><tr><td id="step"><a style="font-weight:bold;">STEP 3:</a></td><td>If you choose manual mode, you have the option of clicking on the original image labels that you want to be deleted.</td></tr><tr><td id="step"><a style="font-weight:bold;">STEP 4:</a></td><td>Save the new labels before continue, otherwise the tool won' + "'" + 't let you press "Next image" button.</td></tr><tr><td id="step" > <a style="font-weight:bold;">STEP 5:</a></td><td>Press "Next image" button once you have saved to continue labeling.</td></tr></table>').appendTo($instructionPopUp)

}

function hide(id) {

  document.getElementById("instructions_bt").remove()

  $('<td id = "td_instructions"><button id = "instructions_bt" onclick="show()" type="button">Show instructions</button></td>').appendTo($tr_menu)

  if (document.body.contains(document.getElementById('instruction_table'))) {

    document.getElementById('instruction_table').remove()

  }

}

function roundToTwo(num) {
  return +(Math.round(num + "e+2")  + "e-2");
}