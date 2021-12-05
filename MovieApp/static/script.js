
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
      document.getElementById('movieForm').submit();
      }
      function getAdvancedOptions()
      {
      event.preventDefault();
      var actor=document.getElementById('advancedActor');
      var ry=document.getElementById('advancedRy');

        actor.style.visibility='visible';
        ry.style.visibility='visible';
      }
