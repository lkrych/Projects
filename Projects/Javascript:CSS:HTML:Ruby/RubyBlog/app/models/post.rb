# == Schema Information
#
# Table name: posts
#
#  id         :integer          not null, primary key
#  title      :string
#  body       :text
#  created_at :datetime         not null
#  updated_at :datetime         not null
#

class Post < ActiveRecord::Base
	has_many :comments, dependent: :destroy #all comments associated with post will be destroyed
	belongs_to :user
	validates_presence_of :title
	validates_presence_of :body
end
