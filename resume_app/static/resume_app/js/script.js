const resumeForm = document.getElementById('resumeForm')

if (resumeForm !== null && resumeForm !== undefined) {
  resumeForm.addEventListener('submit', function (event) {
    event.preventDefault();
    this.submit();
  });
}

const button = document.getElementById('download-button');

window.jsPDF = window.jspdf.jsPDF;
window.html2canvas = html2canvas;

var specialElementHandlers = {
  '.no-expert': function (element, renderer) {
    return true
  }
}

function generatePDF() {

  const { jsPDF } = window.jspdf;

  let doc = new jsPDF('p', 'mm', 'a4');
  let pdfjs = document.querySelector('#content');
  doc.html(pdfjs, {
    callback: function (doc) {
      doc.save("newpdf.pdf");
    },
    margin: [10, 10, 10, 10],

    autoPaging: 'text',
    x: 0,
    y: 0,
    width: 210, //target width in the PDF document
    height: 297,
    windowWidth: 1200	 //window width in CSS pixels
  });

}

button.addEventListener('click', generatePDF);