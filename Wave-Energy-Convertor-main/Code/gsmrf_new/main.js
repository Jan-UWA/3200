function readURL(input) {
  // if (input.files && input.files[0]) {
  var reader = new FileReader();
  reader.onload = function(e) {
    $('.image-upload-wrap').hide();
    $('.file-upload-image').attr('src', e.target.result);
    $('.file-upload-content').show();
    var allowedExtensions = /(\.txt|\.csv|\.png|\.jpg)$/i;
    if (input.files[0] && input.files[1]) {
      if (!allowedExtensions.exec(input.files[0].name) || !allowedExtensions.exec(input.files[1].name)) {
        $('.image-title').html("Invalid file extension(s). Refer to the above instructions");
        $('.digitise-image').hide();
      } else {
        $('.image-title').html(input.files[0].name + " uploaded <br>");
        $('.image-title').append(input.files[1].name + " uploaded <br>");
        $('.digitise-image').show();
      }
    } else {
      if (!allowedExtensions.exec(input.files[0].name)) {
        $('.image-title').html("Invalid file extension(s). Refer to the above instructions");
        $('.digitise-image').hide();
      } else {
        $('.image-title').html(input.files[0].name + " uploaded <br>");
        $('.digitise-image').show();
      }

    }
  };
  if (input.files[0] && input.files[1]) {
    reader.readAsDataURL(input.files[0]);
    reader.readAsDataURL(input.files[1]);
  } else {
    reader.readAsDataURL(input.files[0]);
  }
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
    var allowedExtensions = /(\.txt|\.csv)$/i;
    var text = input.files[0].name;
    var ext = text.slice(-3);
    console.log(text);
    // if (!allowedExtensions.exec(input.files[0].name)) {
    if ((ext != 'csv') && (ext != 'txt')) {
      $('.image-title-csv').html("file tidak cocok");
      $('.digitise-image').hide();
    } else {
      $('.image-title-csv').html(input.files[0].name + " uploaded");
    }

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

// function digitiseUpload() {
//   $('.file-upload').hide();
//   $('#show-digitise').removeClass("is-hidden");
// }

function check() {
  if ($('#technology').val() != "" && $('#orientationsize').val() != "" && $('#modemotion').val() != "" && $('#method').val() != "" && $('#submerged').val() != "") {
    $('#submit-btn').removeAttr('disabled');
    $('#submit-btn').addClass('btn-blue');
    $('#submit-btn').removeClass('btn-grey');
  } else {
    $('#submit-btn').attr('disabled', true);
    $('#submit-btn').addClass('btn-grey');
    $('#submit-btn').removeClass('btn-blue');
  }
}

function checkstep2() {
  if ($('#unitx').val() == "k" && ($('#unity').val() == "pkw" || $('#unity').val() == "pw")) {
    if ($('#unitx').val() != "" && $('#k').val() != "" && $('#unity').val() != "" && $('#incident').val() != "" && $('#designperiod').val() != "" && $('#lowercutoff').val() != "" && $('#uppercutoff').val() != "") {
      $('#step2-submit-btn').removeAttr('disabled');
      $('#step2-submit-btn').addClass('btn-blue');
      $('#step2-submit-btn').removeClass('btn-grey');
    } else {
      $('#step2-submit-btn').attr('disabled', true);
      $('#step2-submit-btn').addClass('btn-grey');
      $('#step2-submit-btn').removeClass('btn-blue');
    }
  } else if ($('#unitx').val() == "tto" && ($('#unity').val() == "pkw" || $('#unity').val() == "pw")) {
    if ($('#unitx').val() != "" && $('#tto').val() != "" && $('#unity').val() != "" && $('#incident').val() != "" && $('#designperiod').val() != "" && $('#lowercutoff').val() != "" && $('#uppercutoff').val() != "") {
      $('#step2-submit-btn').removeAttr('disabled');
      $('#step2-submit-btn').addClass('btn-blue');
      $('#step2-submit-btn').removeClass('btn-grey');
    } else {
      $('#step2-submit-btn').attr('disabled', true);
      $('#step2-submit-btn').addClass('btn-grey');
      $('#step2-submit-btn').removeClass('btn-blue');
    }
  } else if ($('#unitx').val() == "lambda" && ($('#unity').val() == "pkw" || $('#unity').val() == "pw")) {
    if ($('#unitx').val() != "" && $('#lambda').val() != "" && $('#unity').val() != "" && $('#incident').val() != "" && $('#designperiod').val() != "" && $('#lowercutoff').val() != "" && $('#uppercutoff').val() != "") {
      $('#step2-submit-btn').removeAttr('disabled');
      $('#step2-submit-btn').addClass('btn-blue');
      $('#step2-submit-btn').removeClass('btn-grey');
    } else {
      $('#step2-submit-btn').attr('disabled', true);
      $('#step2-submit-btn').addClass('btn-grey');
      $('#step2-submit-btn').removeClass('btn-blue');
    }
  } else if (($('#unitx').val() != "lambda" && $('#unitx').val() != "k" && $('#unitx').val() != "tto") && ($('#unity').val() == "pkw" || $('#unity').val() == "pw")) {
    if ($('#unitx').val() != "" && $('#unity').val() != "" && $('#incident').val() != "" && $('#designperiod').val() != "" && $('#lowercutoff').val() != "" && $('#uppercutoff').val() != "") {
      $('#step2-submit-btn').removeAttr('disabled');
      $('#step2-submit-btn').addClass('btn-blue');
      $('#step2-submit-btn').removeClass('btn-grey');
    } else {
      $('#step2-submit-btn').attr('disabled', true);
      $('#step2-submit-btn').addClass('btn-grey');
      $('#step2-submit-btn').removeClass('btn-blue');
    }
  } else if ($('#unitx').val() == "k" && ($('#unity').val() != "pkw" && $('#unity').val() != "pw")) {
    if ($('#unitx').val() != "" && $('#k').val() != "" && $('#unity').val() != "" && $('#designperiod').val() != "" && $('#lowercutoff').val() != "" && $('#uppercutoff').val() != "") {
      $('#step2-submit-btn').removeAttr('disabled');
      $('#step2-submit-btn').addClass('btn-blue');
      $('#step2-submit-btn').removeClass('btn-grey');
    } else {
      $('#step2-submit-btn').attr('disabled', true);
      $('#step2-submit-btn').addClass('btn-grey');
      $('#step2-submit-btn').removeClass('btn-blue');
    }
  } else if ($('#unitx').val() == "tto" && ($('#unity').val() != "pkw" && $('#unity').val() != "pw")) {
    if ($('#unitx').val() != "" && $('#tto').val() != "" && $('#unity').val() != "" && $('#designperiod').val() != "" && $('#lowercutoff').val() != "" && $('#uppercutoff').val() != "") {
      $('#step2-submit-btn').removeAttr('disabled');
      $('#step2-submit-btn').addClass('btn-blue');
      $('#step2-submit-btn').removeClass('btn-grey');
    } else {
      $('#step2-submit-btn').attr('disabled', true);
      $('#step2-submit-btn').addClass('btn-grey');
      $('#step2-submit-btn').removeClass('btn-blue');
    }
  } else if ($('#unitx').val() == "lambda" && ($('#unity').val() != "pkw" && $('#unity').val() != "pw")) {
    if ($('#unitx').val() != "" && $('#lambda').val() != "" && $('#unity').val() != "" && $('#designperiod').val() != "" && $('#lowercutoff').val() != "" && $('#uppercutoff').val() != "") {
      $('#step2-submit-btn').removeAttr('disabled');
      $('#step2-submit-btn').addClass('btn-blue');
      $('#step2-submit-btn').removeClass('btn-grey');
    } else {
      $('#step2-submit-btn').attr('disabled', true);
      $('#step2-submit-btn').addClass('btn-grey');
      $('#step2-submit-btn').removeClass('btn-blue');
    }
  } else {
    if ($('#unitx').val() != "" && $('#unity').val() != "" && $('#designperiod').val() != "" && $('#lowercutoff').val() != "" && $('#uppercutoff').val() != "") {
      $('#step2-submit-btn').removeAttr('disabled');
      $('#step2-submit-btn').addClass('btn-blue');
      $('#step2-submit-btn').removeClass('btn-grey');
    } else {
      $('#step2-submit-btn').attr('disabled', true);
      $('#step2-submit-btn').addClass('btn-grey');
      $('#step2-submit-btn').removeClass('btn-blue');
    }
  }
}
$(document).ready(function() {
  // step 3
  $('#technology').keyup(check());
  $('#orientationsize').change(check());
  $('#modemotion').change(check());
  $('#method').change(check());
  $('#characteristic').keyup(function() {
    if ($("#characteristic").val() != "") {
      if (!$.isNumeric($('#characteristic').val())) {
        $('#error-characteristic').html("Please enter number only and use . (dot) for decimal");
      } else {
        $('#error-characteristic').html("");
      }
    } else {
      $('#error-characteristic').html("");
    }
  });
  $('#submerged').keyup(function() {
    if ($("#submerged").val() != "") {
      if (!$.isNumeric($('#submerged').val())) {
        $('#error-submerged').html("Please enter number only and use . (dot) for decimal");
      } else {
        $('#error-submerged').html("");
        check();
      }
    } else {
      $('#error-submerged').html("");
      check();
    }
  });
  $('#depth').keyup(function() {
    if ($("#depth").val() != "") {
      if (!$.isNumeric($('#depth').val())) {
        $('#error-depth').html("Please enter number only and use . (dot) for decimal");
      } else {
        $('#error-depth').html("");
      }
    } else {
      $('#error-depth').html("");
    }
  });
  //end of step 3
  //step 2
  $('#unitx').change(function() {
    if ($('#unitx').val() == "k") {
      $('#k-form-group').show();
      $('#tto-form-group').hide();
      $('#lambda-form-group').hide();
    } else if ($('#unitx').val() == "tto") {
      $('#k-form-group').hide();
      $('#tto-form-group').show();
      $('#lambda-form-group').hide();
    } else if ($('#unitx').val() == "lambda") {
      $('#k-form-group').hide();
      $('#tto-form-group').hide();
      $('#lambda-form-group').show();
    } else {
      $('#k-form-group').hide();
      $('#tto-form-group').hide();
      $('#lambda-form-group').hide();
    }
    checkstep2();
  });
  $('#k').keyup(function() {
    if ($("#k").val() != "") {
      if (!$.isNumeric($('#k').val())) {
        $('#error-k').html("Please enter number only and use . (dot) for decimal");
      } else {
        $('#error-k').html("");
        checkstep2();
      }
    } else {
      $('#error-k').html("");
      checkstep2();
    }
  });
  $('#tto').keyup(function() {
    if ($("#tto").val() != "") {
      if (!$.isNumeric($('#tto').val())) {
        $('#error-tto').html("Please enter number only and use . (dot) for decimal");
      } else {
        $('#error-tto').html("");
        checkstep2();
      }
    } else {
      $('#error-tto').html("");
      checkstep2();
    }
  });
  $('#lambda').keyup(function() {
    if ($("#lambda").val() != "") {
      if (!$.isNumeric($('#lambda').val())) {
        $('#error-lambda').html("Please enter number only and use . (dot) for decimal");
      } else {
        $('#error-lambda').html("");
        checkstep2();
      }
    } else {
      $('#error-lambda').html("");
      checkstep2();
    }
  });
  $('#unity').change(function() {
    if ($('#unity').val() == "pkw" || $('#unity').val() == "pw") {
      $('#incident-form-group').show();
    } else {
      $('#incident-form-group').hide();
    }
    checkstep2();
  });
  $('#incident').keyup(function() {
    if ($("#incident").val() != "") {
      if (!$.isNumeric($('#incident').val())) {
        $('#error-incident').html("Please enter number only and use . (dot) for decimal");
      } else {
        $('#error-incident').html("");
        checkstep2();
      }
    } else {
      $('#error-incident').html("");
      checkstep2();
    }
  });
  $('#designperiod').keyup(function() {
    if ($("#designperiod").val() != "") {
      if (!$.isNumeric($('#designperiod').val())) {
        $('#error-designperiod').html("Please enter number only and use . (dot) for decimal");
      } else {
        $('#error-designperiod').html("");
        checkstep2();
      }
    } else {
      $('#error-designperiod').html("");
      checkstep2();
    }
  });
  $('#lowercutoff').keyup(function() {
    if ($("#lowercutoff").val() != "") {
      if (!$.isNumeric($('#lowercutoff').val())) {
        $('#error-lowercutoff').html("Please enter number only and use . (dot) for decimal");
      } else {
        $('#error-lowercutoff').html("");
        checkstep2();
      }
    } else {
      $('#error-lowercutoff').html("");
      checkstep2();
    }
  });
  $('#uppercutoff').keyup(function() {
    if ($("#uppercutoff").val() != "") {
      if (!$.isNumeric($('#uppercutoff').val())) {
        $('#error-uppercutoff').html("Please enter number only and use . (dot) for decimal");
      } else {
        $('#error-uppercutoff').html("");
        checkstep2();
      }
    } else {
      $('#error-uppercutoff').html("");
      checkstep2();
    }
  });
});