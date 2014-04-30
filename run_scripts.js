 $(function() {
           $('#run-python').click(function(e){
               var url = '192.168.56.101/Gene_Family_Visualization/gene_locations.py';
               $.ajax({
                       type: "GET",
                       url: url,
               }).done(function(results){
                       $('#ajax-div').empty().append(results);
               });
          });
       });