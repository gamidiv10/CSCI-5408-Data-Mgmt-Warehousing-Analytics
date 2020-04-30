function wordMap()
{
    var singlewords = this.Tweet_Text.toLowerCase().match(/\w+/gi);

    if(singlewords == null)
    {
        return;
    }

    for(var i=0; i<singlewords.length; i++)
    {
        emit(singlewords[i], {count:1});
    }

}