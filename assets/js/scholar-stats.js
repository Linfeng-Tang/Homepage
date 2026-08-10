/* Render the latest Scholar snapshot without requiring a site redeployment. */
(function () {
  "use strict";
  var currentScript = document.currentScript;
  var dataUrl = new URL("../data/scholar.json", currentScript.src);
  fetch(dataUrl, { cache: "no-store" })
    .then(function (response) { return response.ok ? response.json() : null; })
    .then(function (stats) {
      if (!stats) return;
      var format = function (value) { return Number(value).toLocaleString("en-US"); };
      document.querySelectorAll("[data-scholar-citations]").forEach(function (item) { item.textContent = format(stats.citations); });
      document.querySelectorAll("[data-scholar-hindex]").forEach(function (item) { item.textContent = format(stats.hindex); });
      document.querySelectorAll("[data-scholar-i10index]").forEach(function (item) { item.textContent = format(stats.i10index); });
    })
    .catch(function () { /* Keep the static fallback values if Scholar data is unavailable. */ });
})();
