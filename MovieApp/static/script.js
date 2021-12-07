
     window.addEventListener('load',()=>
     {
     document.getElementById('movieThumbnail').addEventListener('mouseover',

        function()
        {
          setTimeout(function()
          {
            //console.log('works');
            var trailer=document.getElementById('trailer');
            var thumbnail=document.getElementById('thumbnail');
            var play_button=document.getElementById('playButton');
            play_button.style.display='none';
            thumbnail.style.display='none';
            trailer.style.display='block';

          },500);

        }
      );
      document.getElementById('movieThumbnail').addEventListener('mouseout',
        function()
        {
          setTimeout(function()
          {
            //console.log('works');
            var trailer=document.getElementById('trailer');
            var thumbnail=document.getElementById('thumbnail');
            var play_button=document.getElementById('playButton');
            play_button.style.display='block';
            thumbnail.style.display='block';
            trailer.style.display='none';

          },500);
          trailer.src=trailer.src;
        }
      );});

      window.addEventListener('load', function ()
      {
        tomatometer=document.getElementById('tomatometer');
        audience=document.getElementById('audience');
        tomatometer_score=parseInt(tomatometer.textContent);
        audience_score=parseInt(audience.textContent);
        counter_audience=parseInt(1);
        counter_tomatometer=parseInt(1);
        var counter = setInterval(function()
        {
              if(counter_tomatometer<=tomatometer_score)
                  tomatometer.textContent=counter_tomatometer++;
              else
                clearInterval(counter);
                //console.log(this.tomatometer_score+' '+this.counter_tomatometer);
        },7);
        var counter2 = setInterval(function()
        {
              if(counter_audience<=audience_score)
                  audience.textContent=counter_audience++;
              else
                clearInterval(counter2);
                //console.log(this.tomatometer_score+' '+this.counter_tomatometer);
        },15);
      });

      function Submit()
      {

      var form=document.createElement("form");
        form.setAttribute('method', "GET");
            form.setAttribute('action',"search");
             form.style.display='none';

      var titlePlaceholder=document.getElementById('titlePlaceholder');
          var actorPlaceholder=document.getElementById('actorPlaceholder');
             var yearPlaceholder=document.getElementById('yearPlaceholder');




      var titleInput=titlePlaceholder.cloneNode(true);
          var actorInput=actorPlaceholder.cloneNode(true);
             var yearInput=yearPlaceholder.cloneNode(true);

                      yearPlaceholder.disabled=true;
                        actorPlaceholder.disabled=true;

                  console.log(titleInput);
                  console.log(actorInput);
                  console.log(yearInput.value);


      var advanced_field=document.getElementById('advancedField');
        var advancedInput=document.createElement('input');
         advancedInput.setAttribute('type','text');
          advancedInput.setAttribute('name','advanced');
            advancedInput.setAttribute('value',advanced_field.getAttribute('on'));

            console.log(advancedInput);

      form.appendChild(titleInput);
      form.appendChild(advancedInput);
      form.appendChild(actorInput);
      form.appendChild(yearInput);
      document.body.appendChild(form);


      form.submit();

      }

      function getAdvancedOptions()
      {

         var advanced_field=document.getElementById('advancedField');
         var button=document.getElementById('advanced');
         var icon=document.getElementById('advancedIcon');

        if(advanced_field.style.display=='none')
         {
            advanced_field.style.display='block';
            advanced_field.setAttribute('on','true');
            button.textContent='Disable';
            icon.classList.remove('advanced_icon');
            icon.classList.add('advanced_icon_spin');
         }
        else if(advanced_field.style.display=='block')
         {
            advanced_field.style.display='none';
            advanced_field.setAttribute('on','false');
            button.textContent='Enable';
            icon.classList.remove('advanced_icon_spin');
            icon.classList.add('advanced_icon');

      }
    }

      function addActor()
      {
        var button=document.getElementById('addActor');
        var placeholder=document.getElementById('actorPlaceholder');

         if(placeholder.style.display=='none')
          {
            placeholder.style.display='block';
            button.textContent='Remove';
          }
          else if(placeholder.style.display=='block')
          {
            placeholder.style.display='none';
            button.textContent='Add';
            placeholder.value='';

          }

      }

       function addYear()
      {
        var button=document.getElementById('addYear');
        var placeholder=document.getElementById('yearPlaceholder');


         if(placeholder.style.display=='none')
          {
            placeholder.style.display='block';
            button.textContent='Remove';
          }
          else if(placeholder.style.display=='block')
          {
            placeholder.style.display='none';
            button.textContent='Add';
            placeholder.value='';
          }

      }

      window.addEventListener('load', function ()
      {
      window.addEventListener('keydown',function(event){
    if(event.keyCode == 13) {
     Submit();
    }
  });
});
