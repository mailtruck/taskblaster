(function(document, window) {
  var iframeId = '__baBupUnAS3';

  var receiveMessage = function(event) {
    window.removeEventListener('message', receiveMessage, false);

    var data = JSON.parse(event.data);

    if (data['code'] == 'auth') {
      console.log(data);
      window.location.href = data['arg1'];
      return;
    }

    var node = document.getElementById(iframeId);
    node.parentNode.removeChild(node);
  };

  window.addEventListener('message', receiveMessage, false);

  var tags = window['___Ju2aHaGUvu__tags']; 

  var iframe = document.createElement('iframe');
  iframe.name = iframeId;
  iframe.id = iframeId;
  iframe.src = document.location.protocol + '$SERVER/savepage.html';
  iframe.setAttribute('style', 'z-index: 2147483647;left:10px;top:10px;position:fixed;width:168px;height:100px;border: 3px solid #aaa;');
  iframe.onload = function() { 
    var data = {};
    data['href'] = document.location.href;
    data['title'] = document.title;
    data['referrer'] = document.referrer;
    data['tags'] = tags;
    window.frames[iframeId].postMessage(JSON.stringify(data), '*');
  };
  document.body.appendChild(iframe);
})(document, window);
