var selectedText = '';
_featureId = [];
_mod_id = 1;
getAndPrintFeatures();
function highlight(startOffset, endOffset)
{
    var range = document.createRange();
    var textElement = document.getElementById('TextSample');
    textElement.innerHTML = strip(textElement.innerHTML);
    range.setStart(textElement.childNodes[0], startOffset);
    range.setEnd(textElement.childNodes[0], endOffset);
    var newNode = document.createElement("strong");
    range.surroundContents(newNode);
}

function strip(html)
{
   var tmp = document.createElement("DIV");
   tmp.innerHTML = html;
   return tmp.textContent || tmp.innerText || "";
}

// Get the modal
var modal = document.getElementById('featureEditor');

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on <span> (x), close the modal
function closeModal() {
    modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target === modal) {
        modal.style.display = "none";
    }
}

//submit form
function submitFeature(){
   var feature = document.getElementById('feature').value;
   var disclosureLocation = document.getElementById('disclosureLocation').value;
   var isDisclosed = document.getElementById('isDisclosed').value;
   var disclosureOpinion = document.getElementById('disclosureOpinion').value;

    $.ajax({
      url: "/experts/feature/submit",
      type: "get",
      data: {feature: feature, disclosureLocation: disclosureLocation, isDisclosed: isDisclosed, disclosureOpinion: disclosureOpinion},
      success: function(response) {
        closeModal();
        getAndPrintFeatures();
      },
      error: function(xhr) {
          console.log(xhr)
          window.alert("Failed to add feature.");
      }
    });
}

//Get list of features
function getAndPrintFeatures(){
    $.ajax({
      url: "/expert1/features/get",
      type: "get",
      data: {},
      success: function(response) {
        printFeatures(response);
      },
      error: function(xhr) {
        window.alert("Failed to get features.");
      }
    });
}

function printFeatures(features){
    var tableElement = document.getElementById('featureList');

    while (tableElement.hasChildNodes()) {
        tableElement.removeChild(tableElement.lastChild);
    }
    for (var i in features){
        var row = '';
        _featureId.push(features[i].id)
        var disclosureLocation1 = features[i].disclosureLocation1
        var disclosureLocation2 = features[i].disclosureLocation2

        row += '<td>'+ features[i].feature +'</td>';
        row += '<td>'+ features[i].isDisclosedA +'</td>';
        row += '<td>'+ features[i].isDisclosedB +'</td>';
        row += '<td>'+ features[i].disclosureOpinionA +'</td>';
        row += '<td>'+ features[i].disclosureOpinionB +'</td>';
        row += '<td><input id="expertOpinion" class="expertOpinion">'+ "" +'</td>';
        row += "<td><button id='highlightBtn' onclick='highlight("+disclosureLocation1.toString()+", " + disclosureLocation2.toString() + ")'>Highlight</button></td>";
        row += '<td><input id="infringementScore" class="infringementScore">'+ "" +'</td>';
        row += '<td><input id="noveltyScore" class="noveltyScore">'+ "" +'</td>';
        tableElement.innerHTML += '<tr>' + row + '</tr>';
    }
}

function deleteFeature(id){
    $.ajax({
      url: "/patentee1/feature/delete",
      type: "get",
      data: {id: id},
      success: function(response) {
          getAndPrintFeatures()
      },
      error: function(xhr) {
          console.log(xhr)
          window.alert("Failed to delete feature.");
      }
    });
}

function submitScores(id) {
    _mod_id = id;
    var expertOpinion = [];
    var list = $( ".expertOpinion" );
    for (var i in list){
        expertOpinion.push(list[i].value);
    }

    var infringementScore = [];
    var list = $( ".infringementScore" );
    for (var i in list){
        infringementScore.push(list[i].value);
    }

    var noveltyScore = [];
    var list = $( ".noveltyScore" );
    for (var i in list){
        noveltyScore.push(list[i].value);
    }

    var inventiveness = $("inventivenessScore").value

    $.ajax({
      url: "/expert1/score/post",
      type: "get",
      data: {modId: _mod_id, featureId: _featureId, expertOpinion: expertOpinion, infringementScore: infringementScore, noveltyScore: noveltyScore},
      success: function(response) {
          getAndPrintFeatures()
      },
      error: function(xhr) {
          console.log(xhr)
          window.alert("Failed to add scores.");
      }
    });
    
}

