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
    // margin: [0, 0, 0, 0],

    autoPaging: 'text',
    x: 0,
    y: 0,
    width: 210, //target width in the PDF document in (mm)
    // height: 297, //target height in the PDF document in (mm)
    windowWidth: 1050	 //window width in CSS pixels
  });

}

button.addEventListener('click', generatePDF);

// button.addEventListener('click', function() {
//   var content = document.querySelector('#content');
//   html2canvas(content, {
//       allowTaint: true,
//       useCORS: true, // Allows cross-origin images to be used
//   }).then(function(canvas) {
//       var imgData = canvas.toDataURL('image/png');
//       var doc = new jsPDF('p', 'mm');
//       doc.addImage(imgData, 'PNG', 10, 10);
//       doc.save('sample.pdf');
//   });
// });