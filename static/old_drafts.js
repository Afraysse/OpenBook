//gets all the drafts saved

function oldDrafts(results) {
    // var status = results;
    // $('#old_drafts').html(status);
    console.log("Added old drafts");

}

function addOldDrafts() {
    $.get("/get_drafts",
        function (data) {
            console.log(data);
            console.log("Acquired data")
        });
}
