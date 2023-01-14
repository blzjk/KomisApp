$(document).ready(function ($) {
    $(document).on('click', '[data-toggle="lightbox"]:not([data-gallery="navigateTo"])', function(event) {
        event.preventDefault();
        return $(this).ekkoLightbox({
            maxWidth: 9999,
            maxHeight: viewPortHeight - 42,
            onShown: function() {
                if (window.console) {
                    return console.log('Test eventu');
                }
            },
            onNavigate: function(direction, itemIndex) {
                if (window.console) {
                    return console.log('Nawigowanie'+direction+'. Bieżący element: '+itemIndex);
                }
            }
        });
    });
});

