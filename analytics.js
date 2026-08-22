(function initMercaTaxGoogleAnalytics() {
  'use strict';

  const MEASUREMENT_ID = 'G-36LMR9ZYWD';
  if (window.__MERCATAX_GA4_INITIALIZED__) return;
  window.__MERCATAX_GA4_INITIALIZED__ = true;

  window.dataLayer = window.dataLayer || [];
  window.gtag = window.gtag || function gtag() {
    window.dataLayer.push(arguments);
  };

  window.gtag('consent', 'default', {
    analytics_storage: 'granted',
    ad_storage: 'denied',
    ad_user_data: 'denied',
    ad_personalization: 'denied'
  });
  window.gtag('js', new Date());
  window.gtag('config', MEASUREMENT_ID, {
    send_page_view: true,
    allow_google_signals: false,
    allow_ad_personalization_signals: false
  });

  const tag = document.createElement('script');
  tag.async = true;
  tag.src = 'https://www.googletagmanager.com/gtag/js?id=' + encodeURIComponent(MEASUREMENT_ID);
  tag.dataset.mercataxGa4 = MEASUREMENT_ID;
  document.head.appendChild(tag);
})();
