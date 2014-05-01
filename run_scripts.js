 $(function() {
           $('#run-python').click(function(e){
               var url = '/Gene_Family_Visualization/gene_locations.py';
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