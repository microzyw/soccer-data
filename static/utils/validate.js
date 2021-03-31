function isEmpty(obj) {
    if (typeof(obj) == undefined) {
        return true;
    } else {
        if (obj == "") {
            return true;
        } else {
            return false;
        }
    }
}