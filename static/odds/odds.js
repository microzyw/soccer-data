$(function() {
    // 初始日期设定
    var nowYmd = getNowYMD();
    $("#matchDay").val(nowYmd);
    // 初期化
    initContentList();
    $(document.body).infinite(100).on("infinite", function() {
        var page = parseInt(getSessionValue(SESSION_HISTORY_PAGE)) + 1;
        var maxPage = parseInt(getSessionValue(SESSION_HISTORY_MAX_PAGE));
        if (page<=maxPage) {
            $("#loadingZone").show();
            getContent(page);
        } else {
            $("#endZone").show();
            $("#loadingZone").hide();
        }
    });
    // 比赛日选择
    $("#matchDay").datetimePicker({
        title: '比赛日选择',
        years:range(2000,2049),
        times:function(){return [];},
        parse:function(str){
            return str.split("-");
        },
        onChange: function (picker, values, displayValues) {
            console.log(values);
        },
        onClose: function(p, v, d) {
            initContentList();
        }
    });
});

function initContentList() {
    $("#loadingZone").show();
    document.getElementById("dataZone").innerHTML = "";
    $("#dataZone").hide();
    $("#endZone").hide();
    setSessionValue(SESSION_HISTORY_PAGE, 1);
    setSessionValue(SESSION_HISTORY_MAX_PAGE, 1);
    getContent(1);
}

function getContent(page) {
    var nowDate = $("#matchDay").val();
    $.ajax({
        async : false,
        type : "post",
        url : "/odds/showmatchlist",
        dataType : "json",
        data: {"page": page, "per": "15", "nowdate": nowDate},
        success: function (data) {
            if (data.success=="false") {
                $.toptip('比赛日数据加载失败，请重试！','error');
                $("#loadingZone").hide();
            } else {
                $("#dataZone").show();
                $.each(data.matchlist, function(index, value){
                    addContentToZone(value);
                });
                setSessionValue(SESSION_HISTORY_PAGE, page);
                setSessionValue(SESSION_HISTORY_MAX_PAGE, data.maxPage);
                $("#loadingZone").hide();
            }
        },
        error:function (data) {
            $.toptip('比赛日数据加载失败，请重试！','error');
            $("#loadingZone").hide();
        }
    });
}

function addContentToZone(object) {
    var content =
        '<a class="weui-cell weui-cell_access" href="javascript:goToDateList(\'' + object + '\');">' +
        '   <div class="weui-cell__bd"><p>' + object + '</p></div>' +
        '   <div class="weui-cell__ft"></div>' +
        '</a>';
    $("#dataZone").append(content)
}