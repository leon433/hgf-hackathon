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

function highlight(startOffset, endOffset)
{
    var range = document.createRange();
    var textElement = document.getElementById('TextSample');
    range.setStart(textElement.childNodes[0], startOffset);
    range.setEnd(textElement.childNodes[0], endOffset);
    var newNode = document.createElement("strong");
    range.surroundContents(newNode);
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
      },
      error: function(xhr) {
        //Do Something to handle error
      }
    });
}


