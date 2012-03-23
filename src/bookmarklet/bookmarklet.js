(function(document, tags) {
  var loadCount = 0;

  var loadBookmarklet = function() {

    var body = document.body;
    if (!body) {
      if (loadCount < 3) {
        setTimeout(loadBookmarklet, ((2^loadCount)*1000));
        loadCount++;
     } else {
        alert('Please wait until the page has loaded.');
        return;
      }
    }

    window['___Ju2aHaGUvu__tags'] = tags

    var script = document.createElement('script');
    script.type = 'text/javascript'
    script.src = document.location.protocol + '$SERVER/js/loader.min.js' +
        '?t=' + (new Date().getTime());
    document.body.appendChild(script);
  }

  loadBookmarklet();
}(document, ['to']));
