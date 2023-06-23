# Functions for reformating data frames



#' Rename the columns in a tibble
#'
#' @param tbl_to_rename Tibble with the original names.
#' @param rename_map Named vector with the map of name changes.
#' @return Tibble with the new column names.
rename_columns <- function(tbl_to_rename, rename_map) {
  for (i in seq_along(rename_map)) {
    col_name <- names(rename_map[i])
    new_col_name <- rename_map[[i]]
    if (col_name %in% names(tbl_to_rename)) {
      names(tbl_to_rename)[
        which(names(tbl_to_rename) == col_name)
      ] <- new_col_name
    }
  }
  return(tbl_to_rename)
}