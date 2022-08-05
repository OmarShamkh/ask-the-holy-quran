class AddChapterIdToTafseer < ActiveRecord::Migration[6.1]
  def change
    add_column :tafseers, :chapter_id, :string
  end
end
