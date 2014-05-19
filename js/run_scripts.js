
/*
 $(function() {
           $('#run-python').click(function(e){
               var url = '/Gene_Family_Visualization/bin/gene_locations.py';
               $.ajax({
                       type: "GET",
                       url: url,
               }).done(function(results){
                      alert("fetch this content");
                      console.log(results)
                       $('#ajax-div').empty().append(results);
               });
          });
       });

 $(function() {
          $('#gene-info').click(function(e){
            var url = '/Gene_Family_Visualization/bin/gene_information.py';
            $.ajax({
                  type: "GET",
                  url: url, 
            }).done(function(results){
                  alert("getting content");
                  console.log(results)
                  $('#ajax-div').empty().append(results);
            });
          });
 });
*/

$(function() {
  $('#gene-info').click(function(e) {
      var url = '../bin/gene_locations.py';
      var term = $('#inputgene').val();
      //alert(term);
      $.ajax({
            type: "POST",
            url: url,
            data: {mygene: term},
            dataType: 'html',
            context: document.body
      }).done(function(response){
            //print("done doing things");
            console.log(response)
            //window.location='./network.html'
            //$('#ajax-div2').empty().append(response);
            //alert(response);//Data files created for sunburst and heatmap views.");
      });
  });
});
/*
$(function(){
    $('#gene-info').click(function(e){
        window.location='./circle.html'
    });
});  
*/