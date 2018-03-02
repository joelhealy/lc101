
function loadData() {

    var $body = $('body');
    var $wikiElem = $('#wikipedia-links');
    var $nytHeaderElem = $('#nytimes-header');
    var $nytElem = $('#nytimes-articles');
    var $greeting = $('#greeting');

    // clear out old data before new request
    $wikiElem.text("");
    $nytElem.text("");

    // load streetview
    var streetVal = $('#street').val();
    var cityVal = $('#city').val();
    // console.log(streetVal + ", " + cityVal);
    var imgString = '<img class="bgimg" src="http://maps.googleapis.com/maps/api/streetview?size=600x300&location=' + streetVal + ', ' + cityVal + '" />';
    // console.log(imgString);
    $body.append(imgString);

    // console.log("Querying the NY Times ...");
    var apikey = "bc53e19fc84b48da817a112e6982c523";

    var url = "https://api.nytimes.com/svc/search/v2/articlesearch.json";
    url += '?' + $.param({
      'api-key': apikey,
      'q': cityVal
    });

    $greeting.text("So you want to live at " + streetVal);
    $nytHeaderElem.text("New York Times Articles for " + cityVal);

    $.getJSON(url, function(data) {
        // console.log(data);
        $.each(data.response.docs, function(index, item) {
            var headline = item.headline.main;
            if (headline.length > 60) {
                headline = headline.substr(0, 60) + " ...";
            }
            var nytListItemStr = '<li><a href="' + item.web_url + '">' + (index + 1) + '</a>&nbsp;&nbsp;' + headline + '</li>';
            // console.log(nytListItemStr);
            $nytElem.append(nytListItemStr);
            
        });
    }).error(function() {
        $nytHeaderElem.text("New York Times Articles Could Not Be Loaded")
    });

    // var url = "https://en.wikipedia.org/w/api.php?action=query&titles=Main%20Page&prop=revisions&rvprop=content&format=json&formatversion=2";
    var url = "https://asdfasdfdf.en.wikipedia.org/w/api.php?action=opensearch&search=" + cityVal + "&format=json&formatversion=2"
    console.log("Querying Wikipedia using " + url);
    $.ajax(
        {
            url: url,
            dataType: 'jsonp',
            success: function(data) {
                console.log("Querying Wikipedia succeeded!");
                // console.log(data);
                // console.log(data[1]);
                data[1].forEach(function(title) {
                    console.log(title);
                    var wikiListItemStr = '<li><a href="https://en.wikipedia.org/w/index.php?title=' + title + '">' + title + '</a></li>';
                    $wikiElem.append(wikiListItemStr);
                });
            }
        }
    )

    return false;
};

$('#form-container').submit(loadData);
