
data_collect_func = """function parse_table(){
                            var table = document.querySelectorAll('.table.table-bordered.background-white.shares-table.fixedHeader')[1];
                            var all_data = [];
                            for(var i =1; i<table['rows'].length; i++){

                                var columns = table['rows'][i].getElementsByTagName('td');
                                var column_data = [];
                                for(var j=0; j<columns.length; j++){
                                    column_data.push(columns[j].innerText.replace(",", ""));
                                }
                                all_data.push(column_data);
                            }
                            return all_data;
                        }
                        return parse_table();"""