function getNowYMD() {
    var nowDate = new Date();
    var year = nowDate.getFullYear();
    var month = ( nowDate.getMonth() + 1 ) < 10 ? '0' + ( nowDate.getMonth() + 1 ) : ( nowDate.getMonth() + 1 );
    var day = nowDate.getDate() < 10 ? '0' + nowDate.getDate() : nowDate.getDate();
    return year + "-" + month + "-" + day;
}

function getDivHeight(didHeihgt) {
    var h = document.documentElement.scrollHeight;
    return h - didHeihgt;
}