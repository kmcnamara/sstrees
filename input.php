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
      $pdbdir = '/home/kylem/BIMM185/pdbs/';
      $newpname = preg_replace("/[^A-Za-z0-9-_]/", "", htmlspecialchars($_POST["pname"]) );
      $output;
      exec( 'stat ' . $pdbdir . $newpname, $output );
      if (count($output) == 0) {
        exec( 'mkdir ' . $pdbdir . $newpname );
        $newids = preg_replace("/[^A-Za-z0-9]/", " ", htmlspecialchars($_POST["ids"]) );
        $res;
        exec( 'python /home/kylem/BIMM185/scripts/getStructures.py ' . $newpname . ' ' . $newids, $res );
        if (count($res) != 0) {
          echo "<div class='alert alert-block alert-error'>";
          echo "<b>Unable to download a .pdb file for the following IDs, " .
               "please remove them or try again.</b>";
          echo "</div>";
          echo "<b>Unable to use these PDB IDs:</b><br>";
          foreach ($res as $i => $value) {
            echo "<b>" . $value . "</b><br>";
          }
          // Get rid of the directory due to failure
          exec( 'rm -r ' . $pdbdir . $newpname );
        }
        else {
          echo "<div class='alert alert-success'>";
          echo "  <a class='close' data-dismiss='alert'>x</a>";
          echo "  <b>All .pdb files located and downloaded.</b>";
          echo "</div>";
          // Split PDB files
          exec( "python /home/kylem/BIMM185/scripts/runsplitPDB.py " . $newpname );
          unset($res);
          exec( 'ls ' . $pdbdir . $newpname, $res );
          // Let user choose which chains to run thru analysis
          echo "<form action='result.php' method='post' id='chains'>";
          echo "<b>Which structure alignment algorithm would you like to use?</b><br><br>";
          echo "<input type='radio' name='algo' value='deep' checked><b>DeepAlign (TM-Score)</b><br>";
          echo "<input type='radio' name='algo' value='tm'><b>TMalign (TM-Score)</b><br>";
          echo "<input type='radio' name='algo' value='fat'><b>FATCAT (Weighted RMSD)</b><br>";
          echo "<input type='radio' name='algo' value='matt'><b>MATT (Weighted RMSD)</b><br>";
          echo "<input type='radio' name='algo' value='click'><b>Click (RMSD)</b><br>";
          echo "<br>";
          echo "<b>Which chains would you like to analyze?</b><br>";
          echo "<b>(Optional: replace names)</b><br>";
          foreach ($res as $i => $value) {
            echo "<input type='checkbox' name='forkeeps[]' value='" . $value . "' /><b>" . $value ;
            echo "</b><br>";
          }
          echo "<br>";
          echo "<input type='hidden' name='pname' value='".$newpname."'>";
          echo "<input type='submit' value='Submit &raquo;' class='btn btn-custom' ";
          $onclick = "this.value='Submitting...';this.disabled='disabled';this.form.submit();";
          echo "onclick=\"".$onclick."\" />";
          echo "<br>";
          echo "</form>";
        }
      }
      else { //That dir exists already, return an error
        echo "<div class='alert alert-block alert-error'>";
        echo "<b>Error: that project name is incompatible or in use, please try again.</b>";
        echo "</div>";
      }

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
