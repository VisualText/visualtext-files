[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# dirlist

## Purpose

List the entries of a directory.

## Syntax

```
returnedArray = dirlist(dirStr)
returnedArray = dirlist(dirStr, patternStr)
```

```
returnedArray - type: str array

dirStr - type: str

patternStr - type: str
```

## Returns

An array of the full paths of the entries in the directory, sorted. Returns an empty array if the directory is empty, if nothing matches the pattern, or if the path is not a directory; a warning is written to the log in that last case.

## Remarks

The results are **full paths**, not bare names, so they feed straight into [readfile](readfile.md), [readlines](readlines.md), [fileexists](fileexists.md) and [filesize](filesize.md) with no path-joining by the analyzer. The paths always use forward slashes, on every platform, so analyzer code that builds or compares them stays portable.

Results are sorted, so a run over a directory is reproducible; the order in which a file system hands back directory entries is not otherwise defined.

The listing is **not** recursive, and it includes subdirectories alongside files. Call [fileexists](fileexists.md) or [direxists](direxists.md) on an entry to tell the two apart.

The optional pattern is a glob matched case-insensitively against the entry **name** only, never against the rest of the path. `*` matches any run of characters, including none, and `?` matches exactly one. A pattern must match the whole name, so `"*.dict"` matches `terms.dict` but `"dict"` matches nothing.

When nothing matches, the result is an empty array. Guard a loop over it by testing the **first element** rather than the count: assigning an empty array to a variable collapses it back to no value, and [arraylength](arraylength.md) reports 1 for a variable holding no value, so a count test would run the loop once over a phantom entry.

```
if (strlength(L("files")[0])) {
    # ... safe to loop ...
}
```

To recover the bare name of an entry, split on `/` and take the last piece, or match it with [refind](refind.md):

```
L("name") = refind(L("path"),"[^/]+$")[0];
```

## Example

```
@CODE

# Load every dictionary sitting in the analyzer's data folder.
L("files") = dirlist(G("$apppath") + "/data", "*.dict");

# Guard on the first element, not the count -- see Remarks.
if (strlength(L("files")[0])) {
    L("len") = arraylength(L("files"));
    L("i") = 0;
    while (L("i") < L("len")) {
        "out.txt" << "loading " << L("files")[L("i")] << "\n";
        L("i")++;
    }
}

@@CODE
```

## See Also

[readfile](readfile.md), [readlines](readlines.md), [direxists](direxists.md), [fileexists](fileexists.md), [File Functions](Table_of_File_Functions.md)
