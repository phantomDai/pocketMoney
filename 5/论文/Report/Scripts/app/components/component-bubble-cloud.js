define(['knockout'], function (ko) {

    function BubbleCloudViewModel(params) {
        var self = this;

        // 属性
        self.similarAuthors = [];

        // 方法
        self.init = function () {
            // 取前8
            var similarAuthorsByOrder = _.sortBy(params.value(), 'CopyPercent').reverse();
            self.similarAuthors = _.first(similarAuthorsByOrder, 8);

            //
            $('.bubbleCloud').on('mouseover', '>.bubblecloud-bubble', function () {
                var index = $(this).data('index');
                var text = $(this).data('text');

                $('.bubblecloud-line')
                    .addClass('bubblecloud-line' + index)
                    .text(text)
                    .show();
            }).on('mouseout', '>.bubblecloud-bubble', function () {
                var index = $(this).data('index');
                $('.bubblecloud-line').hide().removeClass('bubblecloud-line' + index);
            }).on('click', '>.bubblecloud-bubble', function () {
                var text = $(this).html();
                if (text != "无") {
                    window.open(app.AuthorLink + 'searchParam=' + text);
                }
            });
        }

        self.init();
    }

    return BubbleCloudViewModel;

});
