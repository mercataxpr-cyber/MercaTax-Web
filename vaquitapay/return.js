// The app opens these pages with ?app=<scheme>; only its own schemes are honoured.
(() => {
  const app = new URLSearchParams(location.search).get("app");
  if (app !== "vaquita" && app !== "vaquita-staging") return;
  for (const link of document.querySelectorAll("[data-vaquita-return]")) {
    link.href = `${app}://`;
  }
  for (const link of document.querySelectorAll('a[href^="/vaquitapay/"]')) {
    if (link.hasAttribute("data-vaquita-return")) continue;
    const url = new URL(link.getAttribute("href"), location.origin);
    url.searchParams.set("app", app);
    link.setAttribute("href", url.pathname + url.search + url.hash);
  }
})();
