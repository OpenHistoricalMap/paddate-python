# paddate.py

Supply the missing month and/or day components of a ISO-formatted date, accounting for negative years (BCE) and for very large dates (-1000000-01-01).

This presumes an infinitely proleptic Gregorian calendar. No underlying date library is used, so dates may exceed the range of Unix epoch, Julian day, et cetera.


### Usage and Examples

```
import paddate

paddate.paddate('1500-05')  # equivalent to paddate('+1500-05', startend='start')
paddate.paddate('1500-05', startend='end')

paddate.paddate('1500')
paddate.paddate('1500', startend='end')

paddate.paddate('1900-02', time='end')  # leap years are supported
paddate.paddate('2000-02', startend='end')

paddate.paddate('-1000000-02')
paddate.paddate('-1000000-02', startend='end')  # leap years are supported way back!
paddate.paddate('-999999-02')
paddate.paddate('-999999-02', startend='end')
```


### Our Use Case and Technical Challenges

At OpenHistoricalMap, we want to lower the barrier to data entry by accepting only partial dates, particularly for ancient events in which specific dates are not known.

While it would be expedient to simply require that contributors supply and `-01-01` or `-12-31`, this would give a false accuracy. Therefore, we have this set of runtime functions which will silently pad out their dates without modifying the underlying records. These "padded" dates could then be used for calculation, stored in a new field, etc.

No underlying date library is used, due to their limitations on date range. Julian-based systems such as PostgreSQL cannot suport dates before 4713 BCE, while Unix epoch-based systems such a `struct tm` are even more limited. As such, a proleptic Gregorian calendar is presumed, even back to ancient history in which the presumed calendar date may have little bearing to the season.
