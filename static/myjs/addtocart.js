function addtocart() {
    var bookid = document.getElementById('bookid').value;
    var qty = document.getElementById('qty').value;
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.status == 200 && this.readyState == 4) {
            // var output = JSON.parse(this.response);
            var output = this.response;
            $('#addmodal').modal('hide');
            document.getElementById('cartvalue').innerHTML = output;
        }
    };
    xml.open('GET', 'addtocart?bookid=' + bookid + "&qty=" + qty, true);
    xml.send();
}



function addmodalcart(pid) {
    $("#bookid").val(pid);
    $('#addmodal').modal('show');
}