function readURL(input) {
  // if (input.files && input.files[0]) {
  var reader = new FileReader();
  reader.onload = function(e) {
    $('.image-upload-wrap').hide();
    $('.file-upload-image').attr('src', e.target.result);
    $('.file-upload-content').show();
    $('.image-title').html(input.files[0].name);
  };
  reader.readAsDataURL(input.files[0]);
  // } else {
  //   removeUpload();
  // }
}

function readURLCSV(input) {
  // if (input.files && input.files[0]) {
  var reader = new FileReader();
  reader.onload = function(e) {
    $('.image-upload-wrap-csv').hide();
    $('.file-upload-image-csv').attr('src', e.target.result);
    $('.file-upload-content-csv').show();
    $('.image-title-csv').html(input.files[0].name);
  };
  reader.readAsDataURL(input.files[0]);
  // } else {
  //   removeUploadCSV();
  // }
}

function removeUpload() {
  // $('.file-upload-input').replaceWith($('.file-upload-input').clone());
  $('.file-upload-content').hide();
  $('.image-upload-wrap').show();
  $('.image-upload-wrap').removeClass('image-dropping');
}

$('.image-upload-wrap').bind('dragover', function() {
  $('.image-upload-wrap').addClass('image-dropping');
});

$('.image-upload-wrap').bind('dragleave', function() {
  $('.image-upload-wrap').removeClass('image-dropping');
});

function removeUploadCSV() {
  // $('.file-upload-input').replaceWith($('.file-upload-input').clone());
  $('.file-upload-content-csv').hide();
  $('.image-upload-wrap-csv').show();
  $('.image-upload-wrap-csv').removeClass('image-dropping');
}

$('.image-upload-wrap-csv').bind('dragover', function() {
  $('.image-upload-wrap-csv').addClass('image-dropping');
});

$('.image-upload-wrap-csv').bind('dragleave', function() {
  $('.image-upload-wrap-csv').removeClass('image-dropping');
});

function digitiseUpload() {
  //$('.file-upload').hide();
  $('.nav').hide();
  $('.home-page').hide();
  $('.about-page').hide();
  // $('#digitised-values').removeClass('is-hidden');
  $('#step2').removeClass('is-hidden');
}

function standardise() {
  $('#q1').hide();
  $('#q2').removeClass('is-hidden');
}

function get_x() {
  $('#q2').hide();
  $('#q3').removeClass('is-hidden');
}

function get_y() {
  $('#q3').hide();
  $('#q4').removeClass('is-hidden'); 
}

function x_k() {
  $('#q3').hide();
  $('#q3.1').removeClass('is-hidden'); 
}

function x_axis() {
  const rbs = document.querySelectorAll('input[name="x_values"]');
  let selectedValue;
  for (const rb of rbs) {
    if (rb.checked) {
      selectedValue = rb.value;
      break;
    } 
  }
  if (selectedValue == "period") {
    get_y();
  }
  else if (selectedValue == "frequency") {
    get_y();
  }
  else if (selectedValue == "rotational_frequency") {
    get_y();
  }
  else if (selectedValue == "k*x") {
    x_k();
  }
}
