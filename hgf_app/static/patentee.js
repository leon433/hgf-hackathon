var selectedText = '';
function getText() {
    selectedText = (document.all) ? document.selection.createRange().text : document.getSelection();

    if(selectedText.toString().length > 0) {
        document.getElementById('feature').value = selectedText.toString();
        document.getElementById('featureInModal').innerHTML = "Feature identified: " + selectedText.toString();

        //"Anchor offset, Focus offset" which is the same as "start_char index, end_char index"
        document.getElementById('disclosureLocation').value = (selectedText.anchorOffset + ", " + selectedText.focusOffset).toString();

        openModal();
    }
}
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

// When the user clicks the button, open the modal
function openModal() {
    modal.style.display = "block";
}

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
      url: "/patentee1/feature/submit",
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
      url: "/patentee1/features/get",
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
        var disclosureLocation1 = features[i].disclosureLocation1
        var disclosureLocation2 = features[i].disclosureLocation2

        row += '<td>'+ features[i].feature +'</td>';
        row += '<td>'+ features[i].isDisclosed +'</td>';
        row += '<td>'+ features[i].disclosureOpinion +'</td>';
        row += "<td><button id='highlightBtn' onclick='highlight("+disclosureLocation1.toString()+", " + disclosureLocation2.toString() + ")'>Highlight</button></td>";
        row += "<td><button id='deleteBtn' onclick='deleteFeature(" + features[i].id + ")'>Delete</button></td>";
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


