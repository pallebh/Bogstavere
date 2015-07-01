function tr_build()
{
	var tr = document.createElement( 'tr' ) ;	
	return tr ;
}

function td_build( value )
{
	var td = document.createElement( 'td' ) ;
	var text = document.createTextNode( value ) ;
 	td.appendChild( text ) ; 
	return td ;
} 

function table_build( list )
{
	console.log( "table_build" )
	var table = document.createElement( 'table' ) ;	
		
	console.log( list.length ) ; 	
		
	var count = 0 
	for( var l in list )
	{
		var tr = tr_build() ; 
		if( count % 2 == 0 )
		{
			tr.setAttribute( "class" , "wordListligth" ) ;
		} 
		else
		{
			tr.setAttribute( "class" , "wordListDarker" ) ;
		}
		
		
		tr.appendChild( td_build( l  ) )
		tr.appendChild( td_build( list[ l ][1] ) )
		tr.appendChild( td_build( list[ l ][0] ) )
		table.appendChild( tr ) ;
		count += 1 ; 
	}
	return table ;
}


jQuery( document ).ready( 
	
	function()
	{
		console.log( "result_list" )
		
		var source = new EventSource('result_list');
   		source.addEventListener('wordListUpdate', 
    	function( event )
		{
			var data = jQuery.parseJSON( event.data ) ;					
			var table = table_build( data ) ; 		
			$( "#wordlist" ).empty()  
			$( "#wordlist" ).append( table ) ;
		}
	,
	false
 	);

	}
) ;


