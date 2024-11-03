#Function for computing Amazon S3 MD5 digest (128 bit base64 encoded) using System.Security.Cryptography.MD5 
#$file=Read-Host "Please input the file:"
function Hash-MD5 ($file) { 
    $cryMD5 = [System.Security.Cryptography.MD5]::Create() 
    $fStream = New-Object System.IO.StreamReader ($file) 
    $bytHash = $cryMD5.ComputeHash($fStream.BaseStream) 
    $fStream.Close() 
    return [Convert]::ToBase64String($bytHash) 
}