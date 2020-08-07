document.addEventListener('DOMContentLoaded', () => {
	
	document.querySelector('#form').onsubmit= () => {
		//iniatialize new requets
		const request = new XMLHttpsRequest();//allow to makw a ajax request to some other web server
		const currency=document.querySelector('#currency').value;
		request.open('POST','/convert');

		//callback funstion when the rquest is done being loaded
		request.onload = ()=>{

			//extract the json data from request
			const data =JSON.parse(request.responseText);

			//upddate the result div
			if(data.success){
				const content =`1 USD is equal to ${data.rate} ${currency}.`;
				document.querySelector('#result').innerHTML=content; 
			}
			else{
				document.querySelector('#result').innerHTML='there was an error.';
			}
		}
		//add data to send with the /convert request
		const data=new formdata();
		data.append('currency',currency);

		//send request
		request.send(data);
		return false;
	}
})