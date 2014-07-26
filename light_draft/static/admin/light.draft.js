(function ($) {
    $(function () {
        var href = location.href + 'preview/',
            button = $('<li><a href="'+href+'" class="previewlink" target="_blank">Draft preview</a></li>');

        $('.object-tools > li > a.viewsitelink')
            .closest('ul')
            .find('li:first')
            .before(button);

        button.click(function () {
            var form = $('form[method="post"][enctype="multipart/form-data"]'),
                link;

            if (window.CKEDITOR) {
                $('textarea').each(function () {
                    var $textarea = $(this),
                        instance = window.CKEDITOR.instances[$textarea.attr('id')];
                    if (instance) {
                        $textarea.val(instance.getData());
                    }
                });
            }

            $.ajax({
                type: "POST",
                url: href,
                data: form.serialize(),
                dataType: 'text',
                async: false,
                success: function (response) {
                    link = response;
                }
            });

            if (link) {
                $(this).children('a').attr('href', link);
                return true;
            }

            alert('An error has occurred');
            return false;
        });
    });
}(jQuery || django.jQuery));
