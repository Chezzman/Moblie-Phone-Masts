// Table Toggle
$(function(){
  $("th").on('click', function(){
    var rows = $("table tbody tr").get();
    rows.sort(sortTable);
    $.each(rows, function(index, row){
      $('table').children("tbody").append(row);
    });
    if (ascending) {
      ascending = false;
    }else {
      ascending = true;
    }
  });
});

var ascending = false;

function sortTable(a,b){
  var A = parseInt($(a).children('td').eq(0).text(), 10);
  var B = parseInt($(a).children('td').eq(0).text(), 10);

if(ascending) {
  if(A > B) return 1;
  if(A < B) return -1;
}else{
  if(A > B) return -1;
  if(A < B) return 1;
}
  return 0;
}
