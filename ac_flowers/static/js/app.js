'use strict';

(function () {
    function init() {
        var router = new Router([
            new Route('explore', 'explore.html', true),
            new Route('bayes', 'bayes.html'),
            new Route('simulate', 'simulate.html')
        ]);
    }
}());
