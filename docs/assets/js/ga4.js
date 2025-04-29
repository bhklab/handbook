window.dataLayer = window.dataLayer || [];
function gtag() {
  dataLayer.push(arguments);
}
gtag('js', new Date());
gtag('config', 'G-GW7GQT08LM');

document$.subscribe(() => {
  gtag('event', 'page_view', {
    page_path: location.pathname + location.search,
    page_location: location.href,
    page_title: document.title
  });
});
