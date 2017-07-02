/**
 * Created by ashish on 7/2/17.
 */

$(document).ready(function () {
          $('.rnotif').click(function (e) {
              course = $(this).attr("value");
              $.ajax({
                  type:'GET',
                  url:'/removenotification/?id='+course,
                  success:function () {
                      alert(course+" - Course removed successfully!!");
                  },
                  error:function () {
                      alert("Something went wrong!!!");
                  }

              })

          })

      })