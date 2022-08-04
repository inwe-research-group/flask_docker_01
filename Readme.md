## Comando en Code para obtener el historial de comando ejecutados
Get-History | Out-File myhistory.txt

## Comandos ejecutados para construir el docker
  Id CommandLine                                                                                          
  -- -----------                                                                                          
   docker build -t flask .                                                                              
   docker images                                                                                        
   docker run -d -p 5000:5000 flask 
   
   Ir al browser y buscar localhost:5000                                                                    

   docker ps                                                                                            
   docker stop feeaddf0c7f3                                                                             
   docker run -d -p 5500:5000 flask                                                                     

   Ir al browser y buscar localhost:5500    
   
   docker stop feeaddf0c7f3                                                                 


