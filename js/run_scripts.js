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