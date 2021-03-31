function submitLogin() {
     var username = $("#username").val();
     var password = $("#password").val();
     if (isEmpty(username)) {
         $.toptip('请输入用户名！','error')
         return false;
     }
     if (isEmpty(password)) {
         $.toptip('请输入密码！','error')
         return false;
     }
     $.showLoading();
     $.ajax({
        async : false,
        type : "post",
        url : "/login/submitlogin",
        dataType : "json",
        data: {"username": username, "password": password},
        success: function (data) {
            if (data.success=="false") {
                $.hideLoading();
                $.toptip('登录失败，请重试！','error')
            } else {
                setSessionValue(SESSION_TOKEN, data.token)
                $.hideLoading();
                window.location.href = "/menu";
            }
        },
        error:function (data) {
            $.hideLoading();
            $.toptip('登录失败，请重试！','error')
        }
    });
}