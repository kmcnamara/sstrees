<!DOCTYPE html>
<html>
<!-- BASE -->
<head>
  <title>SVS</title>
  <meta name="svs">
  <link rel="shortcut icon" href="img/favicon.ico">
  <!-- Bootstrap -->
  <link href="css/override.css" rel="stylesheet" media="screen">
</head>
<body>

  <script src="js/bootstrap.min.js"></script>
  <div class="navbar navbar-fixed-top top-bar-font">
    <div class="navbar-inner navbar-style">

      <div class="container user-container">
        <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse"> <span class="icon-bar"></span> <span class="icon-bar"></span> <span class="icon-bar"></span>
        </a> <a class="brand" href="index.html">SVS</a>
        <div class="nav-collapse">
          <ul id="nav-link" class="nav nav-style">
            <li class="divider-vertical"></li>
            <li><a href="index.html">Home</a></li>
            <li class="divider-vertical"></li>
            <li><a href="analysis.html">Analysis</a></li>
            <li class="divider-vertical"></li>
            <li><a href="about.html">About</a></li>
            <li class="divider-vertical"></li>
            <li><a href="contact.html">Contact</a></li>
            <li class="divider-vertical"></li>
          </ul>
        </div>
      </div>
    </div>
  </div>
<!-- END BASE -->

  <div class="container user-container">
  <br><br><br>
  <div class="row">
   <div class="span1">
   </div>
   <div class="span6">
   <div class="well">
    <h2>Sequence Versus Structure</h2>
    <br>

    <?php
      $pname = htmlspecialchars($_POST['pname']) ;
      $pdbdir = '/home/kylem/BIMM185/pdbs/'.$pname;
      $chains = $_POST['forkeeps'];
      // Check which chains the user picked
      if(empty($chains)) {
        echo "<div class='alert alert-block alert-error'>";
        echo "<b>Error: you did not choose any chains for analysis.</b>";
        echo "</div>";
      }
      else {
        $allchains;
        // Print chain file names to a list file
        for($i=0; $i < count($chains); $i++) {
          $allchains = $allchains.' '.$chains[$i];
        }
        exec( 'python /home/kylem/BIMM185/scripts/makeChainFile.py '.$pdbdir.' '.$allchains );
      }
      // Run the algorithm (both seq and struct), just provide project directory and algo
      exec( 'python /home/kylem/BIMM185/scripts/masterHandle.py '.$pdbdir.' '.$_POST['algo'] );
      $sttree = 'temp/'.$pname.'_struct.gif';
      $sqtree = 'temp/'.$pname.'_seq.gif';
      // Present the final results
      echo "<h4>Results:</h4><br>";
      echo "<b>Sequence-based tree:</b><br>";
      echo "<div class='thumbnail'>";
      echo "  <a href=".$sqtree.">";
      echo "  <img src=".$sqtree." width='400' height='300' /></a>";
      echo "</div><br>";
      echo "<b>Structure-based tree:</b><br>";
      echo "<div class='thumbnail'>";
      echo "  <a href=".$sttree.">";
      echo "  <img src=".$sttree." width='400' height='300' /></a>";
      echo "</div><br>";

      exec( 'rm -r ' . $pdbdir );
    ?>

   </div><!--End Well-->
   </div>
  </div> <!--End row-->
  </div> <!--End container-->

</body>

<script type="text/javascript" src="//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
<script type="text/javascript" src="js/bootstrap.min.js"></script>
<script type="text/javascript" src="js/bootstrap-button"></script>
<script type="text/javascript" src="js/bootstrap-alert"></script>

</html>
