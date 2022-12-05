function add_user(){
    $.ajax({
        url: '/add',
        type: 'post',
        data: {
            name : $("#add-name").val(),
            password : $("#add-password").val(),
        },
        success: function(addrow){
          var response = addrow.response
          var name = response.name
          var password = response.password
          var id = response._id
          $("#users").append("<tr><td>"+id+"</td><td>"+name+"</td><td>"+password+"</td><tr>")
        }

    })
}

function delete_row(e){
    var button = $(e.target);
    var id = button.attr("data-id");
    $.ajax({
        url: '/delete/' + id,
        type: 'DELETE',
        success: function(erase){
            $("#"+id).remove();
        }
    })
}

function edit_row(g){
    console.log("edit")
    var button = $(g.target);
    var id = button.attr("data-id");
    var data_obj = {
        name : $("#edit-name-"+id).val(),
        password : $("#edit-password-"+id).val(),
    }
    $.ajax({
        url: '/edit_profile/' + id,
        type: 'PUT',
        data: data_obj,
        success: function(editrow){                
            var response = editrow.response
            var row = $("#"+id)
            row.find(".name").text(response.name)
            row.find(".password").text(response.password)
        }
    })
}

for (const button of document.querySelectorAll('.delete-button')) {
    button.addEventListener('click', delete_row);
}

//$('#add-button').addEventListener('click', add_user)

for (const button of document.querySelectorAll('.edit-button')) {
    button.addEventListener('click', edit_row);
}

const add = document.getElementById("add-button");
add.addEventListener('click', add_user);