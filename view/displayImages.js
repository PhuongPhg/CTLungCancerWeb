function displayImages(path){
   const pcontainer = document.querySelector('.content');
   const container = pcontainer.querySelector('.row');
   fetch(path)
   .then(response => {return response.json()})
   .then(data => {
      let imagesPerColumn = data.length/3;
      var column = []
      for (var i=0;i<3;i++){
         column[i] = document.createElement('div');
         column[i].className = "column";
      }
      
      for (var i=0; i<data.length; i++){
         let div = document.createElement('div');
         div.className="card"; 
         div.innerHTML=
         `
         <a href=${data[i].Link} target="_blank">
            <div class="image">
               <img src=${data[i].Link} alt="image">
            </div>
         </a>
         <div class="img-text">
            <div class="img-description">${data[i].Title}</div>
         </div>
         `
         column[i%3].appendChild(div);
      };
      
      for (var i=0;i<3;i++){
         container.appendChild(column[i])
      }
   })
}