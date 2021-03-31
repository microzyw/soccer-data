function isSessionStorage() {
    if (window.sessionStorage) {
        return true;
    } else {
        return false;
    }
}

function setSessionValue(key, value) {
    sessionStorage.setItem(key, value);
}

function getSessionValue(key) {
    return sessionStorage.getItem(key) || '';
}