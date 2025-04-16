document.getElementById("submitbtn").addEventListener("click",function(e){
    e.preventDefault();

    var Title = document.getElementById("title").value;
    var Desc = document.getElementById("desc").value;

    $.ajax({
        type: "POST",
        url: "/",
        data: {"title" : Title,
                "desc" : Desc},
        success: function () {
                    $("#table").load(location.href + " #table")
                    $("#inputform").load(location.href + " #inputform")
                },

    })
});

document.getElementById("searchbtn").addEventListener("click",function(){
    alert("didnt have time to implement search feature")
})

$(document).on("click", ".delete-btn", function(e) {
    e.preventDefault();

    const todoId = $(this).data("id");
    const $row = $(this).closest("tr");
    $.ajax({
        type: "POST",
        url: `/delete/${todoId}`,
        success: function(response) {
            if (response.success) {
                $row.remove(); 
                $("#table").load(location.href + " #table")
                console.log(response.message);
            }
        },
        error: function(error) {
            console.log("Delete failed", error);
        }
    });
});