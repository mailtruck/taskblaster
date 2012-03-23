var serializeData = function(data) {
  var output = '';
  data = JSON.parse(data);
  for (var key in data) {
    if (!data.hasOwnProperty(key)) {
      continue;
    }
    var val = data[key];
    if (Object.prototype.toString.call(val) === '[object Array]') {
      val = val.join(',');
    }
    if (output.length > 0) {
      output += '&';
    }
    output += encodeURIComponent(key) + '=' + encodeURIComponent(val);
  }
  return output;
};

var endMessage = function(msg) {
  document.getElementById('content').innerHTML = msg;
};

var closeMe = function(opt_code) {
  var code = opt_code || 'ok';
  var data = {};
  data['code'] = code
  if (arguments.length > 1) {
    for (var i = 1; i < arguments.length; i++) {
      data['arg' + i] = arguments[i];
    }
  }
  setTimeout(function() { window.parent.postMessage(JSON.stringify(data), '*'); }, 500);
};

var receiveMessage = function(event) {
  var post_data = serializeData(event.data);
  var xhr = new XMLHttpRequest();
  xhr.open('POST', '/bookmarklet/post', false);
  xhr.onload = function() {
    if (xhr.status == 200) {
      endMessage('Saved!');
      closeMe();
      return;
    }
  }
  xhr.onerror = function() {
    endMessage('Signing in...');
    closeMe('auth', 'http:$SERVER/bookmarklet/post?' + post_data);
  }
  xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
  xhr.send(post_data);
}

window.addEventListener('message', receiveMessage, false);

