class AddChapterIdToAya < ActiveRecord::Migration[6.1]
  def change
    add_column :ayas, :chapter_id, :integer
  end
end
