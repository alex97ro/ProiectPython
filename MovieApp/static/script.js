
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

      function submit()
      {

      var form=document.getElementById('movieForm');
      var button=document.getElementById('advanced');
      var advanced_field=document.getElementById('advancedField');
      var ry_field=document.getElementById('ryField');
      var actor_field=document.getElementById('actorField');
      var advanced=document.createElement('input');
      advanced_field.disabled=true;
      actor_field.style.display='none';
      ry_field.style.display='none';
      advanced.style.display='none';
      advanced.setAttribute('type','text');
      advanced.setAttribute('name','advanced');
      advanced.setAttribute('value',advanced_field.getAttribute('on'));
      form.appendChild(advanced);
      form.appendChild(ry_field);
      form.appendChild(actor_field);
      form.submit();

      }

      function getAdvancedOptions()
      {

         var advanced_field=document.getElementById('advancedField');
         var button=document.getElementById('advanced');
         var ry_field=document.getElementById('ryField');
         var ryButton=document.getElementById('addRy');
         var actor_field=document.getElementById('actorField');
         var actorButton=document.getElementById('addActor');

        if(advanced_field.style.display=='none')
         {
            advanced_field.style.display='block';
            advanced_field.setAttribute('on','true');
            button.textContent='-';
         }
        else if(advanced_field.style.display=='block')
         {
            advanced_field.style.display='none';
            advanced_field.setAttribute('on','false');
            button.textContent='+';
            ry_field.style.display='none';
            ryButton.textContent='+';
            actor_field.style.display='none';
            actorButton.textContent='+';
         }
      }

      function addActor()
      {
        var actor_field=document.getElementById('actorField');
        var button=document.getElementById('addActor');

         if(actor_field.style.display=='none')
          {
            actor_field.style.display='block';
            button.textContent='-';
          }
          else if(actor_field.style.display=='block')
          {
            actor_field.style.display='none';
            button.textContent='+';
          }

      }

       function addRy()
      {
        var ry_field=document.getElementById('ryField');
        var button=document.getElementById('addRy');

         if(ry_field.style.display=='none')
          {
            ry_field.style.display='block';
            button.textContent='-';
          }
          else if(ry_field.style.display=='block')
          {
            ry_field.style.display='none';
            button.textContent='+';
          }

      }

      window.addEventListener('load', function ()
      {
      window.addEventListener('keydown',function(event){
    if(event.keyCode == 13) {
     submit();
    }
  });
});