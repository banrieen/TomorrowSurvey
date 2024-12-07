function Get-MD5([System.IO.FileInfo] $file = $(throw 'Usage: Get-MD5
[System.IO.FileInfo]')) 
{ 
  $stream = $null;   $cryptoServiceProvider = [System.Security .Cryptography .MD5CryptoServiceProvider];
  $hashAlgorithm = new-object $cryptoServiceProvider 
  $stream = $file.OpenRead(); 
  $hashByteArray = $hashAlgorithm.ComputeHash($stream); 
  $stream.Close(); 
  ## We have to be sure that we close the file stream if any exceptions are thrown. 
  trap
  { 
    if ($stream -ne $null) 
    { 
      $stream.Close(); 
    } 
    break; 
  } 
  return [string]$hashByteArray; 
}

